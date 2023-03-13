#Import flask 
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save reference to the table
Precipitation = Base.classes.precipitation

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"

     
        
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation over past last 12 months"""
    # Query 
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '20160824').\
        filter(Measurement.date < '20170824').\
        order_by(Measurement.date).all()

    session.close()

  # Create a dictionary from the row data and append to a list of all_passengers
    precipitation_data = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["Date"] = date
        precipitation_dict["Precipitation"] = precipitation
        precipitation_all.append(precipitation_dict)

    return jsonify(precipitation_data)

      
@app.route("/api/v1.0/station")
def station():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query     
    results = session.query(Station, Station.station).all()
        
    session.close()

    # Convert into list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

                
@app.route("/api/v1.0/tobs")
def tobs():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs"""    
    # Query     
    results =  session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '20160824').\
        filter(Measurement.date < '20170824').\
        order_by(Measurement.date).all()
        
    session.close()    
    
    # Convert into list
    stations_temp_list = list(np.ravel(results))  
        
    return jsonify(stations_temp_list)    


@app.route("/api/v1.0/<start>/<end>")        
def start_end
    # Create session (link) from Python to the DB
    session = Session(engine)
        
    #Query    
    sel = [func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)]
   
    results = session.query(*sel).\
        filter(Measurement.station).\
        filter(Measurement.date >= '20160824').\
        filter(Measurement.date < '20170824').all()

    session.close() 
        
if __name__ == '__main__':
    app.run(debug=True)

          
           