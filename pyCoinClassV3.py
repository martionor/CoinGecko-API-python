from pycoingecko import CoinGeckoAPI
from datetime import *
from tkinter import *

#Run the file ,interface is done in tkinter
#App done by Martin Balogh

cg= CoinGeckoAPI()
root= Tk()
root.title("PyCoinApp")
root.geometry("600x600")

class pyCoin:
    def __init__(self,master):
      myFrame= Frame(master)
      myFrame.pack()

      self.priceDecrease=0
      self.previousArvo=0
      self.priceDecreaseDate=0
      self.info=0
      #List number of days when price decreased
      self.decreaseDays=[]
      #List of dates between price decreased
      self.decreaseDates=[]

      #List of highest total volumes
      self.MaxCost=[]
      #List of date and time when was highest total volumes
      self.TimeAika=[]

      #List for calculating highest price
      self.maxPrice=[]
      #List of timestamps for calculating highest price
      self.timestampMaxPrice=[]

      #List of lowest prices and their timestamps
      self.lowCostlist=[]
      self.dateTimeLowCostList = []

      self.myButton = Button(master, text ="Save date", command=self.clicker)
      self.myButton.place(x=150, y=75)

      self.myButton1 = Button(master, text ="Search CoinGecko", command=self.searchCoingGecko, state=DISABLED)
      self.myButton1.place(x=250, y=75)
      
      self.myButton2 = Button(master, text ="Get days with longest price decrease", command=self.getLongestDecrease,state=DISABLED)
      self.myButton2.place(x=200, y=105)
      
      self.myButton3 = Button(master, text ="Get day with highest tradin volumes and value eur", command=self.totalVolume,state=DISABLED)
      self.myButton3.place(x=170, y=140)
      
      self.myButton5 = Button(master, text ="Get day to buy (date/time)", command=self.getDayToBuy,state=DISABLED)
      self.myButton5.place(x=160, y=180)
      
      self.myButton6 = Button(master, text ="Get day to sell (date/time", command=self.getDayToSell,state=DISABLED)
      self.myButton6.place(x=310, y=180)
      
      self.myButton4 = Button(master, text ="Clear All", command=self.clearAll, background='red', fg='white')
      self.myButton4.place(x=375, y=75)
      
      self.dateEntryStart= Entry(master, width= 50)
      self.dateEntryStart.insert(END,"Write starting date in format yyyy-mm-dd")
      self.dateEntryStart.place(x=150, y=0)

      self.dateEntryEnd= Entry(master, width= 50)
      self.dateEntryEnd.insert(END,"Write ending date in format yyyy-mm-dd")
      self.dateEntryEnd.place(x=150, y=25)

      self.writeDigitalCurrency= Entry(master, width= 50)
      self.writeDigitalCurrency.insert(END,"Choose digital currency name(small letters)")
      self.writeDigitalCurrency.place(x=150, y=50)

      self.startingDateLabel=Label(master,width = 20, text="First day")
      self.startingDateLabel.place(x=175,y=320)

      self.startingDateLabelData=Label(master,width = 20, text="First day")
      self.startingDateLabelData.place(x=175,y=340)

      self.endingDateLabel=Label(master,width = 10, text="Last day")
      self.endingDateLabel.place(x=325,y=320)

      self.endingDateLabelData=Label(master,width = 10, text="Last day")
      self.endingDateLabelData.place(x=325,y=340)
      
      self.decreaseLabel=Label(master,width = 100, text="Longest price decrease days/dates")
      self.decreaseLabel.place(x=-55,y=380)
      
      self.totalVolumeLabel=Label(master,width = 100, text="Highest Total Volume Price/Date")
      self.totalVolumeLabel.place(x=-55,y=410)
      
      self.dayToBuy=Label(master,width = 100, text="Day to buy/time")
      self.dayToBuy.place(x=-55,y=440)
      
      self.dayToSell=Label(master,width = 100, text="Day to sell/time")
      self.dayToSell.place(x=-55,y=470)

      self.digitalCurrencyLabel=Label(master, width=50, text="Digital currency not chosen yet")
      self.digitalCurrencyLabel.place(x=125,y=300)

      self.explainLabel=Label(master, width=50, background= 'red',fg='white',text="First enter the dates \n after that digital currency name \n and click save date button")
      self.explainLabel.place(x=120,y=240)


    def clicker(self):
      self.fullStartingDate= self.dateEntryStart.get() + " 00:00:00+00:00"
      self.dateStart= datetime.strptime(self.fullStartingDate, "%Y-%m-%d %H:%M:%S%z")
      self.tsStart= self.dateStart.timestamp()
      self.fullEndingDate= self.dateEntryEnd.get() + " 23:59:59+00:00"
      self.dateEnd= datetime.strptime(self.fullEndingDate, "%Y-%m-%d %H:%M:%S%z")
      self.tsEnd=self.dateEnd.timestamp()
      self.digitalCurrency=self.writeDigitalCurrency.get()
      self.startingDateLabelData.config(text=self.dateEntryStart.get())
      self.endingDateLabelData.config(text=self.dateEntryEnd.get())
      self.digitalCurrencyLabel.config(text="Currency: " +self.writeDigitalCurrency.get())
      self.myButton1.config(state=NORMAL)
      self.explainLabel.config(text= "Now click search CoinGecko button")

    def clearAll(self):
      self.priceDecrease=0
      self.previousArvo=0
      self.priceDecreaseDate=0
      self.info=0
      self.decreaseDays=[]
      self.decreaseDates=[]
      self.MaxCost=[]
      self.TimeAika=[]
      self.maxPrice=[]
      self.timestampMaxPrice=[]
      self.lowCostlist=[]
      self.dateTimeLowCostList = []
      self.myButton1.config(state=DISABLED)
      self.myButton2.config(state=DISABLED)
      self.myButton3.config(state=DISABLED)
      self.myButton5.config(state=DISABLED)
      self.myButton6.config(state=DISABLED)
      self.explainLabel.config(text="First enter the dates \n after that digital currency name \n and click save date button")
      self.dateEntryStart.delete(0, 'end')
      self.dateEntryEnd.delete(0, 'end')
      self.writeDigitalCurrency.delete(0, 'end')
      self.dateEntryStart.insert(END,"Write starting date in format yyyy-mm-dd")
      self.dateEntryEnd.insert(END,"Write ending date in format yyyy-mm-dd")
      self.writeDigitalCurrency.insert(END,"Choose digital currency name(small letters)")
      self.decreaseLabel.config(text="Longest price decrease days/dates")      
      self.totalVolumeLabel.config(text="Highest Total Volume/Date")      
      self.dayToBuy.config(text="Day to buy/time")      
      self.dayToSell.config(text="Day to sell/time")

    def searchCoingGecko(self):
      self.info=cg.get_coin_market_chart_range_by_id(id=self.digitalCurrency, vs_currency='eur', from_timestamp=self.tsStart ,to_timestamp=self.tsEnd)
      print(self.info)
      self.myButton2.config(state=NORMAL)
      self.myButton3.config(state=NORMAL)
      self.myButton5.config(state=NORMAL)
      self.myButton6.config(state=NORMAL)

    def getStartDate(self):
      tulos= input("Please write date in yyyy-mm-dd format:")
      return(tulos)

    def getEndDate(self):
        tulos1= input("Please write date in yyyy-mm-dd format:")
        return(tulos1)



    def getLongestDecrease(self):
        previousPrice=None
        num=0
        for i in self.info['prices']:
            price=i[1]
            timestampp=i[0]
            dt_object = datetime.utcfromtimestamp(timestampp/1000).replace(microsecond=0)
            if dt_object.strftime("%H:%M:%S") >"23:00:00" and dt_object.strftime("%H:%M:%S")<="23:59:59" or dt_object.strftime("%H:%M:%S") =="00:00:00":
                if previousPrice is not None and price < previousPrice:
                    # print(previousPrice)
                    num +=1
                    # print(dt_object)
                    # print(price)
                    #print(num)
                    self.decreaseDates.append(dt_object.strftime("%Y:%m:%d"))
                else:
                    if num!= 0:
                        #print(num)
                        self.decreaseDates.append(num)
                        self.decreaseDays.append(num)
                    #print("")
                    num=0
                previousPrice = price
        #print(max(decreaseDays))
        self.maxDaysDecrease=max(self.decreaseDays)
        # if self.maxDaysDecrease in self.decreaseDates:
        for i in range(len(self.decreaseDates)):
          if i ==self.maxDaysDecrease:
              self.maxDaysDecreaseIndex=(self.decreaseDates.index(self.maxDaysDecrease))
              self.endingDateDescend=(self.decreaseDates[self.maxDaysDecreaseIndex-1])
              self.startingDateDescend=(self.decreaseDates[self.maxDaysDecreaseIndex-self.maxDaysDecrease])
        print(self.decreaseDates)
        self.decreaseLabel.config(text="Longest price decrease for " +str(self.maxDaysDecrease) +" days, from: " + str(self.startingDateDescend)+ " to "+ str(self.endingDateDescend))

    def totalVolume(self):
        for i in (self.info['total_volumes']):
            maxCost=i[1]
            timeAika=i[0]
            self.MaxCost.append(maxCost)
            self.TimeAika.append(timeAika)
        print(self.MaxCost)
        maxcostindex=self.MaxCost.index(max(self.MaxCost))

        print(max(self.MaxCost))
        price=max(self.MaxCost)
        timeDate= self.TimeAika[maxcostindex]
        timePrint= datetime.utcfromtimestamp(timeDate/1000).replace(microsecond=0)
        print(timePrint)
        self.totalVolumeLabel.config(text="TotalVolume/: " +str(price) +" euro, date/time: "+ str(timePrint))

    def getDayToBuy(self):
        for i in (self.info['prices']):
            lowCost=i[1]
            timeLowCost=i[0]
            self.lowCostlist.append(lowCost)
            self.dateTimeLowCostList.append(timeLowCost)

        self.lowCostNow=min(self.lowCostlist)
        self.minCostNowIndex=self.lowCostlist.index(self.lowCostNow)
        self.timestampLowCost=self.dateTimeLowCostList[self.minCostNowIndex]
        self.dateTimeLowCostConvert=datetime.utcfromtimestamp(self.timestampLowCost/1000).replace(microsecond=0)

        self.dayToBuy.config(text="Best price to buy: "+ str(self.lowCostNow)+ ", date/time: "+ str(self.dateTimeLowCostConvert) )



    def getDayToSell(self):
      for j in (self.info['prices']):
            maxCostp =j[1]
            timestampMaxCost=j[0]
            self.maxPrice.append(maxCostp)
            self.timestampMaxPrice.append(timestampMaxCost)
        
      self.maxCostNow=max(self.maxPrice)
      self.maxCostNowIndex=self.maxPrice.index(self.maxCostNow)
      self.timestampMaxCost=self.timestampMaxPrice[self.maxCostNowIndex]
      self.dateTimeHighCostConvert=datetime.utcfromtimestamp(self.timestampMaxCost/1000).replace(microsecond=0)

      self.dayToSell.config(text="Best price to sell: "+ str(self.maxCostNow)+ ", date/time: "+ str(self.dateTimeHighCostConvert) )

e=pyCoin(root)

root.mainloop()