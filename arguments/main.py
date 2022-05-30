# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name,message ='Hello, <name>!'):
    return message.replace('<name>',name)

def force(mass, body = 'earth'):
    bodies = {'sun':274, 'jupiter':24.92,'neptune': 11.15, 'saturn': 10.44,'earth':9.798, 'uranus': 8.87, 'venus': 8.87, 'mars': 3.71, 'mercury':3.7, 'moon':1.62, 'pluto':0.58}
    return round(bodies[body.lower()],1)*mass

def pull(m1,m2,d): 
    return ((m1*m2)/d**2)*6.674e-11

