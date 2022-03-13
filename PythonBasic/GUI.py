from tkinter import Tk, ttk, Label, Button, Text, END

StationFares = [
    {"station" : "A", "fare" : 1500},
    {"station" : "B", "fare" : 1800},
    {"station" : "C", "fare" : 2100},
    {"station" : "D", "fare" : 2900},
]

selectedIndex = 0

def stationfares_selected(event):
    global selectedIndex
    for item in treestationfares.selection():
        selectedIndex = int(treestationfares.item(item, "text"))
    stationfare = StationFares[selectedIndex]
    station = stationfare["station"]
    fare = str(stationfare["fare"])
    text_Station.delete("1.0", END)
    text_Station.insert("end", station)
    text_Fare.delete("1.0", END)
    text_Fare.insert("end", fare)

def setTreeItems():
    global selectedIndex
    treestationfares.delete(*treestationfares.get_children())
    for index, staionfare in enumerate(StationFares):
        station = staionfare["station"]
        fare = staionfare["fare"]
        treestationfares.insert("", "end", iid=None, text=str(index), values=[station, fare])

def insert_content():
    station = text_Station.get("1.0", END)
    fare = int(text_Fare.get("1.0", END))
    stationfare = {"station" : station, "fare" : fare}
    StationFares.append(stationfare)
    setTreeItems()

def update_content():
    global selectedIndex
    station = text_Station.get("1.0", END)
    fare = int(text_Fare.get("1.0", END))
    selectedItem = StationFares[selectedIndex]
    selectedItem["station"] = station
    selectedItem["fare"] = fare
    setTreeItems()

def delete_content():
    global selectedIndex
    StationFares.pop(selectedIndex)
    setTreeItems()
    return


window = Tk()
window.title("Station Fare Management")
window.geometry("600x600")
window.resizable(0,0)
title = "정류장 요금관리"
lbl_title = Label(window, text=title, font=("돋움체", 20))
lbl_title.pack(padx=5, pady=7)

# 정류장 요금관리 표시 treeStationfares
treestationfares = ttk.Treeview(window)
treestationfares["columns"] = ("station", "fare")
treestationfares.column("#0", width=50)
treestationfares.column("station", width=200)
treestationfares.column("fare", width=150)
# treeStationfares에 순번, 정류장, 요금 표시
treestationfares.heading("#0", text="순번")
treestationfares.heading("station", text="정류장")
treestationfares.heading("fare", text="요금")
treestationfares.place(x=100, y=100, width=400, height=250)
# 검색한 정류장 요금을 선택하면 stationfares_selected 실행
treestationfares.bind("<<TreeviewSelect>>", stationfares_selected)

btn_Insert = Button(window, text="Insert", command=insert_content, font=("돋움체, 14"))
btn_Insert.place(x=100, y=400, width=100, height=30)

btn_Update = Button(window, text="Update", command=update_content, font=("돋움체, 14"))
btn_Update.place(x=250, y=400, width=100, height=30)

btn_Delete = Button(window, text="Delete", command=delete_content, font=("돋움체, 14"))
btn_Delete.place(x=400, y=400, width=100, height=30)


labelStation = Label(window, text="정류장")
labelStation.place(x=100, y=450, width=50, height=25)
labelFare = Label(window, text="요금")
labelFare.place(x=100, y=500, width=50, height=25)

text_Station = Text(window, width=30, height=1)
text_Station.place(x=200, y=450)
text_Fare = Text(window, width=30, height=1)
text_Fare.place(x=200, y=500)

# treeStationfares 초기입력
setTreeItems()

window.mainloop()

