# Wersja bez png
from fpdf import FPDF
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy
from PIL import Image
from io import BytesIO
from urllib.parse import quote
from urllib.request import urlopen
from class_file.Tablica_pokryc import DostepneMetody
from class_file.InputData import InputData
from class_file.Schema import Schema


class PDF(FPDF):

    def __init__(self, zmienne, minterm, dontcare):
        super().__init__()
        self.tab = DostepneMetody(zmienne, minterm, dontcare)

    def basic_table(self, headings, rows):
        for heading in headings:
            self.cell(40, 7, heading, 1)
        self.ln()
        for row in rows:
            for col in row:
                self.cell(40, 6, col, 1)
            self.ln()

    def colored_table(self, headings, rows, szer=55, nazwa='', prawda=False, y=None, x=None, grupa=False):
        self.cell(0, 10, '')
        self.ln()
        self.cell(0, 10, nazwa)
        self.ln()
        line_width = self.line_width
        if not prawda:
            self.set_fill_color(15, 111, 198)
            self.set_text_color(255)
            self.set_draw_color(15, 111, 198)
            self.set_line_width(0.3)
            # self.set_font(style="B")
        print(headings)
        if len(headings[0].split(' ')) > 1:
            splited_x = [x.split(' ') for x in headings]
            x = [x[0] for x in splited_x]
            y = [y[1] for y in splited_x]
            for x_ in x:
                self.cell(szer, 10, x_, "TLR", 0, "B", True)
            self.ln()
            for y_ in y:
                self.cell(szer, 10, y_, "BLR", 0, "T", True)
        else:
            if prawda:
                self.set_fill_color(255, 255, 255)
                self.set_text_color(0)
                for i, heading in enumerate(headings):
                    # self.set_line_width(1)

                    if i == len(headings) - 1:
                        self.cell(1, 7, '', "LB", 0, "C")
                        # self.set_font(style='B')
                        self.cell(szer, 7, heading, "LB", 0, "C")
                    else:
                        self.cell(szer, 7, heading, "B", 0, "C")
            else:
                for heading in headings:
                    self.cell(szer, 10, heading, 55, 0, "C", True)


        # self.set_line_width(line_width)
        self.ln()
        # Color and font restoration:
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font()
        fill = False
        if prawda:
            for row in rows:
                for i, row_ in enumerate(row):
                    if i == len(row) - 1:
                        # self.set_font(style='B')
                        self.cell(1, 8, '', "L", 0, "C", markdown=True)
                        self.cell(szer, 8, row_, "L", 0, "C", markdown=True)
                    else:
                        self.cell(szer, 8, row_, "", 0, "C")
                self.set_font()
                self.ln()
                fill = not fill
        else:
            szerx = [x[0] for x in rows]
            if grupa:
                items = []
                print(rows)
                for row in rows:
                    for i, row_ in enumerate(row):
                        if i == 0:
                            zm = row_ if row_ not in items else ''
                            items.append(row_)
                            if zm:
                                self.cell(szer, 8 * szerx.count(row_) , 'Grupa '+zm, "TLR", 0, "C", fill)
                            else:
                                self.cell(szer, 8, zm, "LR", 0, "C", fill)
                        else:
                            self.cell(szer, 8, row_, "TLR", 0, "C", fill)
                    self.ln()
                    if not grupa:
                        fill = not fill
            else:
                for row in rows:
                    for row_ in row:
                        self.cell(szer, 8, row_, "LR", 0, "C", fill)

                    self.ln()
                    fill = not fill
        if not prawda:
            self.cell(len(headings)*szer, 0, "", "T")
        self.ln()

    def napis(self):
        self.ln()
        df = self.tab.get_tablica_prawdy()
        minterm = df.index[df.Y == 1].tolist()
        dontcare = df.index[df.Y == 'X'].tolist()

        lblMin = ', '.join([str(int) for int in minterm])
        lblDont = ', '.join([str(int) for int in dontcare])
        lblVar = ''
        for idx in list(self.tab.get_tablica_prawdy().columns):
            lblVar += idx[0] if len(idx) == 1 else idx[0] + '_{' + (('').join(idx[1:])) + '}'
            lblVar += ', '
        text = "$f\,(" + lblVar[:-2] + ") = \\sum\,m(" + lblMin + ")"
        if len(dontcare) > 0:
            text += "\,+\,d(" + lblDont + ")"
        text += "$"

        formula = text
        height = 170
        url = f"https://chart.googleapis.com/chart?cht=tx&chs={height}&chl={quote(formula)}"
        with urlopen(url) as img_file:
            img = BytesIO(img_file.read())

        self.image(img, w=100)
        self.ln()
        # self.cell(0, 10, "")
        # self.ln()

    def grupowanie(self):
        df = self.tab.get_pierwsza_grupa()
        # df.rename(columns={"Liczba Dziesiętna": "Liczba Dziesietna"}, inplace=True)
        df.rename(columns={"Liczba Dziesiętna": "Dziesietna",
                           "Liczba Binarna": "Binarna",
                           "Liczba jedynek": "Grupa"}, inplace=True)
        df = df.astype(str)
        headings = list(df.columns)
        rows = df.values.tolist()
        return self.colored_table(headings, rows, nazwa='Wektory:', szer=30, grupa=True)

    def tablica_prawdy(self):
        df = self.tab.get_tablica_prawdy()
        df = df.astype(str)
        headings = list(df.columns)
        rows = df.values.tolist()
        return self.colored_table(headings, rows, nazwa='Tablica prawdy:', szer=10, prawda=True)

    def tablica_pokryc(self):
        df = self.tab.get_tab_pokryc()
        print(df)
        df = df.astype(str)
        headings = list(df.columns)
        rows = df.values.tolist()
        return self.colored_table(headings, rows, nazwa='Tablica pokryc:', szer=15, x=100, y=100)


getVariable = 'A B C D'
getMinterm = '0 1 2 3 4  '
getDontCare = '5, 6'
implikanty = ['0-0-', '-0-1']

pdf = PDF(getVariable, getMinterm, getDontCare)
pdf.set_font("helvetica", size=14)
pdf.add_page()

# 3 --
obj = InputData(getVariable, getMinterm, getDontCare)
schema = Schema(getVariable, implikanty, obj.getTruthTable())
schema.GenerateSchema()
schema.DrawInputs()
schema.DrawGatesAndInput()
schema.DrawGateOr()
schema.DrawKmap()

fig2 = Figure(figsize=(7, 5), dpi=200)
canvas2 = FigureCanvas(fig2)
axes2 = fig2.gca()
axes2.axis("off")
schema.MainSchema.draw(ax=axes2, show=False)
axes2.axis("equal")
canvas2.draw()
img2 = Image.fromarray(numpy.asarray(canvas2.buffer_rgba()))
# 3 --

pdf.image(img2, -20, 150, w=250)
pdf.napis()
y_tab_pokryc = pdf.y
pdf.tablica_prawdy()
xx, yy = pdf.x, pdf.y
pdf.set_left_margin(100)
pdf.set_y(y_tab_pokryc)
pdf.grupowanie()
pdf.tablica_pokryc()
pdf.output("TworzePDF.pdf")