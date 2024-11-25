import requests
import tkinter
def getPrice():
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price"
    querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl"}
    headers = {
        "x-rapidapi-key": "f14036c0b1msh14810e2a39bb53bp1b29d7jsn3ae04cec78bf",
        "x-rapidapi-host": "coinranking1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    price = response.json()['data']['price']
    label.config(text=f"BTC Price: {price}$")
screen = tkinter.Tk()
screen.title('BTC Price Tracker')
screen.geometry("400x300")
screen.config(padx=20, pady=20, bg="#1D1B2A")  # Dark purple base
label_color = "yellow"
button_color = "#5D3A5A"
text_color = "white"
label = tkinter.Label(screen, text="Click the button to get BTC price", fg=label_color, bg="#1D1B2A", font=("default", 14))
label.grid(row=0, column=0, pady=20)
button = tkinter.Button(screen, text="Get BTC Price", command=getPrice, bg=button_color, fg=text_color, relief="ridge", borderwidth=1)
button.grid(row=1, column=0, pady=10)
button.config(width=20, height=2)
screen.mainloop()
