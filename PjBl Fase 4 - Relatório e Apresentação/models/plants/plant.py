from models import db, Sensor


class Plant(db.Model):
    __tablename__ = "plants"
    id_plant = db.Column(db.Integer(), primary_key=True)
    id_sensor = db.Column(db.Integer(), db.ForeignKey(Sensor.id_sensor))
    name = db.Column(db.String(50), nullable=False)
    min_humidity = db.Column(db.Float(), nullable=False)


    def insert_plant(id_sensor, name, min_humidity):
        plant =  Plant(id_sensor=id_sensor, name=name,
                       min_humidity=min_humidity)
        db.session.add(plant)
        db.session.commit()
        return plant
    
    ''' 
    def update_plant(id_plant, id_sensor, name, min_humidity):
        plant = Plant.get_plant(id_plant)
        if id_sensor:
            plant.id_sensor = id_sensor
        if name:
            plant.name = name
        if min_humidity:
            plant.min_humidity = min_humidity
        db.session.commit()
        return plant
    '''
    def update_plant(id_plant, name, id_sensor, min_humidity):
        plant = Plant.get_plant(id_plant)

        if plant:
            #plant.name = name
            plant.id_sensor = id_sensor
            plant.min_humidity = min_humidity
            db.session.commit()
            return plant
        else:
            return False

    def get_plant(id_plant):
        plant = Plant.query.filter_by(id_plant=id_plant).first()
        return plant


    def get_plants():
        plants = Plant.query.all()
        return plants

    ''' 
    def get_plants_joined(id_plant):
        return Plant.query.join(Sensor, Sensor.id_sensor == Plant.id_sensor)\
            .add_columns(Plant.id_plant, Plant.name, Plant.min_humidity, Sensor.id_sensor, Sensor.name.label("name_sensor"))\
            .filter_by(id_plant=id_plant)
    
    '''
    def get_plants_joined():
        return Plant.query.join(Sensor, Sensor.id_sensor == Plant.id_sensor)\
            .add_columns(Plant.id_plant, Plant.name, Plant.min_humidity, Sensor.id_sensor, Sensor.name.label("name_sensor"))
   
    def delete_plant(id_plant):
        try:
            plant = Plant.query.get(id_plant)
            db.session.delete(plant)
            db.session.commit()
            return True
        except:
            return False
       