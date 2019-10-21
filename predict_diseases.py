# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:01:44 2019

@author: ABARNA DEVI
"""

import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import load_model
class predict:
    def predict_disease(segmented):        
        classifier = load_model('new_disease.h5')        
        labels = {0:'Apple___Apple_scab',1:'Apple___Black_rot',2:'Apple___Cedar_apple_rust',3:'Apple___healthy',4:'Blueberry___healthy',5:'Cherry_(including_sour)___Powdery_mildew',6:'Cherry_(including_sour)___healthy',7:'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',8:'Corn_(maize)___Common_rust_',9:'Corn_(maize)___Northern_Leaf_Blight',10:'Corn_(maize)___healthy',11:'Grape___Black_rot',12:'Grape___Esca_(Black_Measles)',13:'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',14:'Grape___healthy',15:'Orange___Haunglongbing_(Citrus_greening)',16:'Peach___Bacterial_spot',17:'Peach___healthy',18:'Pepper,_bell___Bacterial_spot',19:'Pepper,_bell___healthy',20:'Potato___Early_blight',21:'Potato___Late_blight',22:'Potato___healthy',23:'Raspberry___healthy',24:'Soybean___healthy',25:'Squash___Powdery_mildew',26:'Strawberry___Leaf_scorch',27:'Strawberry___healthy',28:'Tomato___Bacterial_spot',29:'Tomato___Early_blight',30:'Tomato___Late_blight',31:'Tomato___Leaf_Mold',32:'Tomato___Septoria_leaf_spot',33:'Tomato___Spider_mites Two-spotted_spider_mite',34:'Tomato___Target_Spot', 35:'Tomato___Tomato_Yellow_Leaf_Curl_Virus',36:'Tomato___Tomato_mosaic_virus',37:'Tomato___healthy'}
        segmented = cv2.resize(segmented,(64,64))
        test_image = image.img_to_array(segmented)        
        test_image = np.expand_dims(test_image, axis = 0)
        test_image = test_image/255        
        result = classifier.predict(test_image)
        disease_detected = labels[np.argmax(result[0],axis=0)]
        cm={"Apple___Apple_scab":" Containing sulfur and pyrethrins, Bonide  Orchard Spray is a safe. For best results, apply as a protective spray (2.5 gallon) early in the season.",
"Apple___Black_Rot":"Use fungicide Bulletin 506 ",
"Apple___Cedar_apple_rust":" Use  SERENADE Garden pesticide for best results.Best of all, SERENADE is completely non-toxic to honey bees and beneficial insects.",
"Apple___healthy":"Healthy",
"Blueberry___healthy":"Healthy",
"Cherry_(including_sour)___powdery_mild":"Use Topsin 4.5 FL at 30 fl oz/A plus another fungicide. Rotate with other fungicides to avoid buildup of resistant fungi.Do not use within 1 day of harvest. Group 1 fungicide. 2-day reentry.",
"Cherry_(including_sour)___healthy":"Healthy",
"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":"Use Metolachlor pesticide- Classified as a Category C herbicide.",
"Corn_(maize)___Common_rust_":"Use Glyphosate- Better known as Monsanto's Roundup, it is used on their companion genetically-modified soy, corn, canola and cotton as well as in home gardens and parks.",
"Corn_(maize)_Northern_Leaf_Blight":"Metam sodium-This widely used fumigant and pesticide is commonly applied to potatoes in concentrations as high as 150 to 300 pounds per acre.",
"Corn_(maize)_healthy":"Healthy",
"Grape___Black_rot":"Throughout the season, while the plants are blooming, people should use strobilurins and sterol inhibitors, such as Nova, Rubigan, Bayleton, Abound, Sovran or Flint. ",
"Grape___Esca_(Black_Measles)":" Remove the infected berries, leaves and trunk and destroy them. Protect the prune wounds to minimize fungal infection using wound sealant (5% boric acid in acrylic paint) or essential oil or suitable fungicides.",
"Grape___healthy":"Healthy",
"Orange___Haunglongbing_(Citrus_greening)":"Use an antibiotic called tetracyclin hydrochloride to reduce the HLB pathogen",
"Peach___Bacterial_spot":"Use an antibiotic called oxytetracyclin as it is least prone to pytotoxicity",
"Peach___healthy":"Healthy",
"Pepper,_bell___Bacterial_spot":"Implement crop rotation strategy and remove all the crop debris at the end of the season and don't make them as compost",
"Pepper,_bell___healthy":"Healthy",
"Potato___Early_blight":"Avoid nitrogen and phosphorus deficiency.Kill vines two to three weeks prior to harvest to allow adequate skin set.",
"Potato___Late_blight":"Avoid planting close to the woods. Windbreaks are not a problem as long as they are not a dense wall of spruce and fir.",
"Potato___healthy":"Healthy",
"Raseberry___healthy":"Healthy",
"Soyabean_healthy":"Healthy",
"Squash___Powdery_mildew":"Crop rotation is a way to reduce the severity. Remove the plant debris. Garden free weeds",
"Strawberry___Leaf_scroch":"Remove the infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants.",
"Strawberry___healthy":"Healthy",
"Tomato___Bacterial_spot":"There is no treatment for the disease once it is detected.To prevent the disease just keep all the affected plants away during the next year",
"Tomato___Early_blight":"Use a chemical fungicide  chlorothalonil . Use an oraganic fungicide copper spray",
"Tomato___Late_blight":"Use a chemical fungicide serenade",
"Tomato___Leaf_Mold":"Milk spray, Garlic spray and corn to prevent fungal breakout",
"Tomato___Septoria_leaf_spot":"Use copper sulphate or copper oxychloride to control the disease",
"Tomato___Spider_mites Two-spotted_spider_mite":"Remove the infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants.",
"Tomato___Target_Spot":"Crop rotation is a way to reduce the severity. Remove the plant debris. Garden free weeds",
"Tomato___Tomato_Yellow_Leaf_Curl_Virus":"Protect seedbeds with a white nylon net (40 mesh).",
"Tomato___Tomato_mosaic_virus":"Sanitation is the most important application to practice when controlling tobacco mosaic virus.",
"Tomato___healthy":"Healthy"} 
        s="disease identified - "+disease_detected+"\nControl measure - "+cm[disease_detected]
        return s