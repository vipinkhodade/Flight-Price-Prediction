from flask import Flask, render_template, request, jsonify
import requests
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model=pickle.load(open('flight.pkl', 'rb'))
@app.route('/', methods=['GET'])
def home():
    return render_template('flight.html')


stndard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    if request.method=='POST':
        
        #departure date
        Journey_date=request.form("Departure_Time")
        Journey_day=int(pd.to_datetime(Journey_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month=int(pd.to_datetime(Journey_date, format="%Y-%m-%dT%H:%M").month)
        
        Dep_hour=int(pd.to_datetime(Journey_date,format="%Y-%m-%dT%H:%M").hour)
        Dep_min=int(pd.to_datetime(Journey_date, format="%Y-%m-%dT%H:%M").min)
        
        #Arrival date
        Arrival_date=request.form("Arrival_Time")
        Arrival_day=int(pd.to_datetime(Arrival_date, format="%Y-%m-%dT%H:%M").day)
        Arrival_month=int(pd.to_datetime(Arrival_date, format="%Y-%m-%dT%H:%M").month)
        
        Arrival_hour=int(pd.to_datetime(Arrival_date, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min=int(pd.to_datetime(Arrival_date, format="%Y-%m-%dT%H:%M").min)
        
        #Duration
        Duration_hours= abs(Arrival_hour-Dep_hour)
        Duration_mins=abs(Arrival_min-Dep_min)
        
        #source
        Source=request.form("Source")
        if (Source=='Banglore'):
            Source_Banglore=1 
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=0
            Source_Mumbai=0
        
        elif (Source=='Chennai'):
            Source_Banglore=0
            Source_Chennai=1
            Source_Delhi=0
            Source_Kolkata=0
            Source_Mumbai=0
            
        elif (Source=='Delhi'):
            Source_Banglore=0
            Source_Chennai=0
            Source_Delhi=1
            Source_Kolkata=0
            Source_Mumbai=0
        elif (Source=='Kolkata'):
            Source_Banglore=0 
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=1
            Source_Mumbai=0

        else:
            Source_Banglore=0
            Source_Chennai=0
            Source_Delhi=0
            Source_Kolkata=0
            Source_Mumbai=1
       
        #Destination
        Destination=request.form("Destination")
        if (Destination=="Banglore"):
            Destination_Banglore=1
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
        
        elif (Destination=="Cochin"):
            Destination_Banglore=0
            Destination_Cochin=1
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
            
        elif (Destination=="Delhi"):
            Destination_Banglore=0
            Destination_Cochin=0
            Destination_Delhi=1
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=0
            
        elif (Destination=="Hyderabad"):
            Destination_Banglore=0
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=1
            Destination_Kolkata=0
            Destination_New_Delhi=0
            
        elif (Destination=="Kolkata"):
            Destination_Banglore=0
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=1
            Destination_New_Delhi=0
            
        else:
            Destination_Banglore=0
            Destination_Cochin=0
            Destination_Delhi=0
            Destination_Hyderabad=0
            Destination_Kolkata=0
            Destination_New_Delhi=1
            
        #total Stops
        Stop=int(request.form('Stops'))
        
        
        #Airlines
        
        Airlines=request.form('Airline')
        if (Airlines=="Airline_Air_Asia"):
            Airline_Air_Asia=1
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Air_India"):
            Airline_Air_Asia=0
            Airline_Air_India=1
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_GoAir"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=1
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_IndiGo"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=1
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Jet_Airways"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=1
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Jet_Airways_Business"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=1
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Multiple_carriers"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=1
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Multiple_carriers_Premium_economy"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=1
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_SpiceJet"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=1
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=0
            
        elif (Airlines=="Airline_Vistara"):
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=1
            Airline_Vistara_Premium_economy=0
            
        else:
            Airline_Air_Asia=0
            Airline_Air_India=0
            Airline_GoAir=0
            Airline_IndiGo=0
            Airline_Jet_Airways=0
            Airline_Jet_Airways_Business=0
            Airline_Multiple_carriers=0
            Airline_Multiple_carriers_Premium_economy=0
            Airline_SpiceJet=0
            Airline_Vistara=0
            Airline_Vistara_Premium_economy=1
                

        prediction=model.predict([[Stop,
                                   Journey_date,
                                   Journey_day, 
                                   Journey_month,
                                   Dep_hour,
                                   Dep_min,
                                   Arrival_hour, 
                                   Arrival_min, 
                                   Duration_hours, 
                                   Duration_mins,
                                   Airline_Air_Asia, 
                                   Airline_Air_India, 
                                   Airline_GoAir,
                                   Airline_IndiGo, 
                                   Airline_Jet_Airways, 
                                   Airline_Jet_Airways_Business,
                                   Airline_Multiple_carriers,
                                   Airline_Multiple_carriers_Premium_economy,
                                   Airline_SpiceJet,
                                   Airline_Vistara, 
                                   Airline_Vistara_Premium_economy, 
                                   Source_Banglore,
                                   Source_Chennai, 
                                   Source_Delhi, 
                                   Source_Kolkata, 
                                   Source_Mumbai,
                                   Destination_Banglore, 
                                   Destination_Cochin, 
                                   Destination_Delhi,
                                   Destination_Hyderabad, 
                                   Destination_Kolkata,
                                   Destination_New_Delhi]])
        
        output=round(prediction[0], 2)
        return render_template('flight.html',prediction_text="Your flight price is RS.{}".format(output))
    else:
        return render_template('flight.html')

if __name__=="__main__":
    app.run()