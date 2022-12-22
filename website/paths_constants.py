"""
@authors
Joris Monnet
Colin Pelletier
Killian Raude
"""
path = {
    "Raw": "img/raw/",
    "Dot": "img/dot/",
    "normal": "img/normal/",
    "Date": "img/date/",
    "Dot and Date": "img/dotdate/",
    "Invisible_Dot": "img/invisible_dot/",
    "logo": "img/logo.png",
    "logo_cropped": "img/logo_cropped.png",
    "date_model": "generated/date_model/",
    "dot_model": "generated/dot_model/",
    "dotDate_model": "generated/dot_model/",
    "invisibleDot_model": "generated/invisibleDot_model/",
    "raw_model": "generated/raw_model/",
}

modelPath = {
    "Raw": path["raw_model"],
    "Dot": path["dot_model"],
    "Date": path["date_model"],
    "Dot and Date": path["dotDate_model"],
    "Invisible_dot": path["invisibleDot_model"],
}

gradcams = {
    "Date": "img/gradcams/date_model/Pneumonia/gradcam.jpeg",
    "Dot": "img/gradcams/dot_model/Pneumonia/gradcam.jpeg",
    "Date_original": "img/gradcams/date_model/Normal/gradcam.jpeg",
    "Raw": "img/gradcams/raw_model/Pneumonia/gradcam.jpeg",
    "Dot and Date": "img/gradcams/dotDate_model/Pneumonia/gradcam.jpeg",
    "Invisible_dot": "img/gradcams/invisible_dot_model/Pneumonia/gradcam.jpeg",
}

absolutePath = "/app/ml-project-2-la_team/"
absolutePathWebsite = absolutePath + "website/"

localPath = "../"
localPathWebsite = "./"
