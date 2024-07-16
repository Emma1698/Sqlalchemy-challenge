# Import the dependencies.
from flask import Flask
import numpy as np 
import datetime as dt 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
#################################################


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup

#################################################




#################################################
# Flask Routes
#################################################
