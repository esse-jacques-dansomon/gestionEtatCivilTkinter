from fpdf import FPDF
from Entity import DeclarationNaissance as d
from Entity.DeclarationNaissance import DeclarationNaissance


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('sn.png', 10, 8, 25, 15)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(50, 10, 'ETAT CIVIL', border=True, ln=1, align='C')
        # Line break
        self.ln(20)
    # Page footer

    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def bodyMaraige(self, nomMo, nomMa, lieu, maire, temoinH, temoinF):
        # Create a PDF object
        pdf = PDF('P', 'mm', 'Letter')

        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        # Add Page
        pdf.add_page()

        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)
        pdf.cell(100, 10, "Nom Du Monsieur")
        pdf.cell(40, 10, f'{nomMo}', ln=1, align="L")
        pdf.cell(100, 10, "Nom De La Femme")
        pdf.cell(40, 10, f'{nomMa}', ln=1, align="L")
        pdf.cell(100, 10, "Lieu Du Mariage")
        pdf.cell(40, 10, f'{lieu}', ln=1, align="L")
        pdf.cell(100, 10, "Celebre par  ")
        pdf.cell(40, 10, f'{maire}', ln=1, align="L" )
        pdf.cell(100, 10, "Temoin Homme")
        pdf.cell(40, 10, f'{temoinH}', ln=1, align="L")
        pdf.cell(100, 10, "Temoin Femmes")
        pdf.cell(40, 10, f'{temoinF}', ln=1, align="L")
        pdf.output("mariage.pdf")

    def declarationNaissance(self, declare):
        # Create a PDF object
        pdf = PDF('P', 'mm', 'Letter')

        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        # Add Page
        pdf.add_page()

        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)
        pdf.cell(100, 10, "Region : ")
        pdf.cell(40, 10, f'{declare.region}', ln=1, align="L")
        pdf.cell(100, 10, "Departement : ")
        pdf.cell(40, 10, f'{declare.departement}', ln=1, align="L")
        pdf.cell(100, 10, "Arraondissent : ")
        pdf.cell(40, 10, f'{declare.arraondissent}', ln=1, align="L")
        pdf.cell(100, 10, "Commune : ")
        pdf.cell(40, 10, f'{declare.commune}', ln=1, align="L")
        pdf.cell(100, 10, "Arraondissent : ")
        pdf.cell(40, 10, f'{declare.arraondissent}', ln=1, align="L")
        pdf.cell(100, 10, "Commune : ")
        pdf.cell(40, 10, f'{declare.commune}', ln=1, align="L")
        pdf.cell(100, 10, "Centre : ")
        pdf.cell(40, 10, f'{declare.centre}', ln=1, align="L")
        pdf.cell(100, 10, "Numero Registre : ")
        pdf.cell(40, 10, f'{declare.numRegistre}', ln=1, align="L")
        pdf.cell(100, 10, "Date de Naissance : ")
        pdf.cell(40, 10, f'{declare.dateNaussence}', ln=1, align="L")
        pdf.cell(100, 10, "Lieu : ")
        pdf.cell(40, 10, f'{declare.lieu}', ln=1, align="L")
        pdf.cell(100, 10, "Sexe  : ")
        pdf.cell(40, 10, f'{declare.sexe}', ln=1, align="L")
        pdf.cell(100, 10, "Nom  : ")
        pdf.cell(40, 10, f'{declare.prenomsEnfant}', ln=1, align="L")
        pdf.cell(100, 10, "Nom Du Pere : ")
        pdf.cell(40, 10, f'{declare.nomPere}', ln=1, align="L"  )
        pdf.cell(100, 10, "Nom De La Mere : ")
        pdf.cell(40, 10, f'{declare.nomMere}', ln=1, align="L")
        pdf.cell(100, 10, "Juge : ")
        pdf.cell(40, 10, f'{declare.juge}', ln=1, align="L")
        pdf.cell(100, 10, "Numero : ")
        pdf.cell(40, 10, f'{declare.numero}', ln=1, align="L")
        pdf.cell(100, 10, "Extrait Delivré par : ")
        pdf.cell(40, 10, f'{declare.centre}', ln=1, align="L")
        pdf.output("declarationNaissance.pdf")

    def extraitNaissancelf(self, declare):
        # Create a PDF object
        pdf = PDF('P', 'mm', 'Letter')
        # get total page numbers
        pdf.alias_nb_pages()

        # Set auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        # Add Page
        pdf.add_page()

        # specify font
        pdf.set_font('helvetica', 'BIU', 16)

        pdf.set_font('times', '', 12)
        pdf.cell(100, 10, "Region : ")
        pdf.cell(40, 10, f'{declare.region}', ln=1, align="L")
        pdf.cell(100, 10, "Departement : ")
        pdf.cell(40, 10, f'{declare.departement}', ln=1, align="L")
        pdf.cell(100, 10, "Arraondissent : ")
        pdf.cell(40, 10, f'{declare.arraondissent}', ln=1, align="L")
        pdf.cell(100, 10, "Commune : ")
        pdf.cell(40, 10, f'{declare.commune}', ln=1, align="L")
        pdf.cell(100, 10, "Centre : ")
        pdf.cell(40, 10, f'{declare.centre}', ln=1, align="L")
        pdf.cell(100, 10, "Numero Registre : ")
        pdf.cell(40, 10, f'{declare.numRegistre}', ln=1, align="L")
        pdf.cell(100, 10, "Date de Naissance : ")
        pdf.cell(40, 10, f'{declare.dateNaussence}', ln=1, align="L")
        pdf.cell(100, 10, "Lieu : ")
        pdf.cell(40, 10, f'{declare.lieu}', ln=1, align="L")
        pdf.cell(100, 10, "Sexe  : ")
        pdf.cell(40, 10, f'{declare.sexe}', ln=1, align="L")
        pdf.cell(100, 10, "Nom  : ")
        pdf.cell(40, 10, f'{declare.nomEnfant}', ln=1, align="L")
        pdf.cell(100, 10, "Prenoms  : ")
        pdf.cell(40, 10, f'{declare.prenomsEnfant}', ln=1, align="L")
        pdf.cell(100, 10, "Nom Du Pere : ")
        pdf.cell(40, 10, f'{declare.nomPere}', ln=1, align="L"  )
        pdf.cell(100, 10, "Nom De La Mere : ")
        pdf.cell(40, 10, f'{declare.nomMere}', ln=1, align="L")
        pdf.output("naissance.pdf")


