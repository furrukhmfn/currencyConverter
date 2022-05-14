
# CREATION OF BASIC CURRENCY CONVERTER
from currency_converter import CurrencyConverter
from tkinter import *
from PIL import ImageTk, Image


c=CurrencyConverter()
root = Tk()
root.title("Currecny Converter ")
root.geometry("600x600")
EmptyLabel=Label(root,text="         ")
# root.iconbitmap('')

# DROP DOWN BOXES 
# DICTONARY-WORK
ListDictonaryofCurrencies={
    "US-Dollar":"USD",
    "Japnesse Yen": "JPY",
    "Bulgarian Lev": "BGN",
    "Czech Koruna": "CZK",
    "Danish Krone":"DKK",
    "Pound sterling": "GBP",
    "Hungarian Forint": "HUF",
    "Poland złoty": "PLN",
    "Romanian Leu": "RON",
    "Swedish krona": "SEK",
    "Swiss Franc": "CNF",
    "Icelandic Króna": "ISK",
    "Norwegian Krone": "NOK",
    "Croatian Kuna": "HRK",
    "Russian Ruble": "RUB",
    "Turkish lira": "TRY",
    "Australian Dollar": "AUD",
    "Brazilian Real": "BRL",
    "Canadian dollar": "CAD",
    "Chinese Yuan":"CNY",
    "Hong Kong Dollar": "HKD",
    "Indonesian Rupiah": "IDR",
    "Israeli New Shekel": "ILS",
    "Indian Rupess": "INR",
    "South Korean won": "KRW",
    "Mexican Peso": "MXN",
    "Malaysian ringgit": "MYR",
    "New Zealand Dollar": "NZD",
    "Philippine peso": "PHP",
    "Singapore Dollar": "SGD",
    "Thai Baht": "THB",
    "South African Rand": "ZAR"


}

def converting():
    # CALCULATION FUNCTION
    global l1
    global l2
    global l3
    global l4
    global l5
    CurrencyValueToBeConverted=EnteryCurrency.get()
    Variable1=clicked.get()
    Varaibel2=clicked1.get()
    EnteryCurrency.delete(0, 'end')
    SecondaryVariabl1=ListDictonaryofCurrencies[Variable1]
    SecondaryVariabl2=ListDictonaryofCurrencies[Varaibel2]
    try:
        convertedvalue=c.convert(CurrencyValueToBeConverted,SecondaryVariabl1,SecondaryVariabl2)
    except:
        print("Function is Not Working....")
        print("Data has been used form Backup Database...")
    convertedvalue=str(convertedvalue)
    # OUTPUT PACK
    l1=Label(root,text="RESULTS", font=("Arial",13))
    l1.place(x=100, y = 280)
    l2=Label(root,text="Input Currency= "+Variable1)
    l2.place(x=200, y = 300)
    l3=Label(root,text="Output Currency="+Varaibel2)
    l3.place(x=200, y=320)
    l4=Label(root,text="Input Currency Value= "+CurrencyValueToBeConverted)
    l4.place(x=200, y=350)
    l5=Label(root,text="Converted Currency Value= "+convertedvalue,font=("Arial",13))
    l5.place(x=200, y=380)
    

def delete1():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    
options=["US-Dollar",
    "Japnesse Yen",
    "Bulgarian Lev",
    "Czech Koruna",
    "Danish Krone",
    "Pound sterling",
    "Hungarian Forint",
    "Poland złoty",
    "Romanian Leu",
    "Swedish krona",
    "Swiss Franc",
    "Icelandic Króna",
    "Norwegian Krone",
    "Croatian Kuna",
    "Russian Ruble",
    "Turkish lira",
    "Australian Dollar",
    "Brazilian Real",
    "Canadian dollar",
    "Chinese Yuan",
    "Hong Kong Dollar",
    "Indonesian Rupiah",
    "Israeli New Shekel",
    "Indian Rupess",
    "South Korean won",
    "Mexican Peso",
    "Malaysian ringgit",
    "New Zealand Dollar",
    "Philippine peso",
    "Singapore Dollar",
    "Thai Baht",
    "South African Rand"
]
# CREATION OF OPTIONS NUMBER 02
options1=["US-Dollar",
    "Japnesse Yen",
    "Bulgarian Lev",
    "Czech Koruna",
    "Danish Krone",
    "Pound sterling",
    "Hungarian Forint",
    "Poland złoty",
    "Romanian Leu",
    "Swedish krona",
    "Swiss Franc",
    "Icelandic Króna",
    "Norwegian Krone",
    "Croatian Kuna",
    "Russian Ruble",
    "Turkish lira",
    "Australian Dollar",
    "Brazilian Real",
    "Canadian dollar",
    "Chinese Yuan",
    "Hong Kong Dollar",
    "Indonesian Rupiah",
    "Israeli New Shekel",
    "Indian Rupess",
    "South Korean won",
    "Mexican Peso",
    "Malaysian ringgit",
    "New Zealand Dollar",
    "Philippine peso",
    "Singapore Dollar",
    "Thai Baht",
    "South African Rand"
]

# WIDGETS
clicked = StringVar()
clicked.set(options[0])
Label(root, text="Input Currency").place(x=100, y=100)
drop = OptionMenu(root,clicked, *options)
drop.place(x=100, y=125)
clicked1 = StringVar()
clicked1.set(options1[0])
Label(root, text="Output Currency").place(x=250, y=100)
drop1= OptionMenu(root,clicked1,*options)
drop1.place(x=250, y=125)
# ENTERY WIDGETS
Label(root,text="Amount").place(x=400, y=100)
EnteryCurrency= Entry(root)
EnteryCurrency.place(x=400, y=130)
myButton = Button(root, text="Calculate Conversion Rates",font=("Arial",15), command=converting).place(x=170, y = 200)
DeleteButton= Button(root, text="Delete Old Conversion", command=delete1).place(x=450, y =550)

# CREATING GRID OF GUI 
Label(root,text="PYTHON CURRENCY CONVERTER",font=("Arial",20)).place(x=70, y =20)

mainloop()