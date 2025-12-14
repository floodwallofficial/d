# -* UTF-8 *-
# Coded by Yumeh's

import sys
import os

# .pop uzantılı dosyaları açma fonksiyonu:
def main():

    # .pop dosyası:
    pop_file = open(f'{sys.argv[1]}','r',encoding='utf-8').read()

    # .pop dosyasını listeye çeviriyoruz:
    pop = pop_file.split("\n")

    # .pop dosyasını değerlendirme:
    for code in pop:
                # If:
        if 'if {' in code:
            code_ = code.replace('if','').replace('{','').replace('}','').replace('<','').replace('>','')
            if 'is' in code_:
                code_ = code_.split('is')
                if code_[0] == code_[1]:
                    w_code = str(code_[2]).replace(',','\n')
                    libfile = open('Lib/executable.lib','w',encoding='utf-8')
                    libfile.write(w_code)
                    libfile.close()
                    os.system('pop.py Lib\executable.lib')
        
        elif 'else <' in code:
            libfile = open('Lib/executable.lib','r',encoding='utf-8').read()
            if libfile == '':
                code_ = code.replace('else <','').replace('>','').replace(',','\n')
                libfile = open('Lib/executable.lib','w',encoding='utf-8')
                libfile.write(code_)
                libfile.close()
                os.system('pop.py Lib\executable.lib')
        # print:
        elif 'print #' in code:
            code_ = code.replace('print #','')
            print(code_)
        
        elif '= print %' in code:
            code_ = code.split('= print %')
            değişken = code_[0] = code_[1]
            print(değişken)

        elif 'print $' in code:
            code_ = code.replace('print $','')
            print(değişken)
        # input:
        elif 'input #' in code:
            code_ = code.replace('input #','')
            input(code_)
        
        elif '= input %' in code:
            code_ = code.split('= input %')
            değişken = code_[0] = code_[1]
            input(değişken)
        
        elif 'input $' in code:
            code_ = code.replace('input $','')
            input(değişken)

        # değişkenler:
        elif '=' in code:
                    
            code_ = code.split('=')
            değişken = code_[0] = code_[1]
            if '"' in değişken or "'" in değişken:
                değişken = değişken.replace('"','')
                değişken = değişken.replace("'","")
            
            else:
                pass


        # Kaçış:
        elif '@' in code:
            pass

        else:
            pass
        

if __name__ == '__main__':
    main()