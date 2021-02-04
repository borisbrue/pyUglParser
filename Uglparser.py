class Uglparser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.project = {}
        self.products = []
        self.process()

    def process_kop(self, line):
        return {
            "kundennummer": line[3:13].strip(),
            "lieferant": line[13:23].strip().strip(),
            "typ": line[23:25].strip().strip(),
            "projekt": line[25:40].strip(),
            "text": line[40:90].strip(),
            "vorgang_gh": line[90:105].strip(),
            "lieferdatum": line[105:113].strip(),
            "dokumentdatum": line[161:169].strip(),
            "waehrung": line[113:116].strip(),
            "ugl_version": line[116:121].strip(),
            "sachbearbeiter": line[121:161].strip(),
        }

    def process_poa(self, position):
        return {
            "nummer_hw": position[3:13].strip(),
            "nummer_gh": position[13:23].strip(),
            "artikelnummer": position[23:38].strip(),
            "menge": position[38:49].strip(),
            "bezeichnung": position[49:90].strip(),
            "bezeichnung2": position[90:129].strip(),
            "einzelpreis": position[129:140].strip(),
            "mengenrabatt": position[140:141].strip(),
            "preis_pro_einheit": position[141:152].strip(),
            "rabatt1": position[152:157].strip(),
            "rabatt2": position[157:162].strip(),
            "lv_nummer": position[162:180].strip(),
            "alternativ_pos": position[180:181].strip(),
            "position_typ": position[181:182].strip(),
            "vb_tech": position[182:183].strip(),
            "mengeneinheit": position[183:186].strip(),
        }

    def process(self):
        with open(self.filepath, "r", encoding="iso-8859-1") as file:
            for line in file.readlines():
                line_type = line[0:3]
                if line_type == "KOP":
                    self.project = self.process_kop(line)
                if line_type == "POA":
                    self.products.append(self.process_poa(line))

    def get_meta(self):
        return self.project

    def get_products(self):
        return self.products
