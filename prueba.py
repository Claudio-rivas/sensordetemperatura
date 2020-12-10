import Adafruit_DHT
import time
import smtplib
from email.mime.text import MIMEText

sensor = Adafruit_DHT.DHT11
gpio = 17
correo_origen = 'claudioestebanrivas@gmail.com'
contraseña = 'lucaslucas12'
correo_destino = 'claudioestebanrivas@gmail.com'
temperatura_umbral = 26

def Enviar_correo(temperatura):
    msg = MIMEText("la temperatura actual se encuentra demasiado alta")
    msg['Subject'] = 'Alerta de Temperatura'
    msg['From'] = correo_origen
    msg['To'] = correo_destino
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(correo_origen,contraseña)
    server.sendmail(correo_origen,correo_destino,msg.as_string())
    print("Su Email ha sido enviado.")
    server.quit()

while True:
    
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, gpio)
    
    if humedad is not None and temperatura is not None:
        print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperatura, humedad))
    
    if temperatura > temperatura_umbral:
            print('aca envia correo')
            Enviar_correo(temperatura)
    
   # else:
   #     print('Fallo de lectura, intente nuevamente')
        
      
        
        
    time.sleep(5)
    