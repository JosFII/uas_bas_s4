import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.markdown(
'''
<style>
    .stApp {
   background-color: white;
    }
 
       .stWrite,.stMarkdown,.stTextInput,h1, h2, h3, h4, h5, h6 {
            color: purple !important;
        }
</style>
''',
unsafe_allow_html=True
)
st.title('Visualisasi pada Big Data')
st.markdown('dibuat oleh: Joseph F.H. (20234920002)')
st.header('Flowchart')
st.image('flw.jpg')
st.header('Data: review game dari platform steam')
st.image('dat1.png')
st.markdown('''
dikarenakan file terlalu besar untuk diupload maka preview menggunakan gambar \n
data merupakan review dari game pada plat form steam yang diambil pada tahun 2020. \n
data diambil dari situs kaggle : https://www.kaggle.com/datasets/najzeko/steam-reviews-2020/data \n
data diambil dengan variabel review sudah di hilangkan karena variabel review, yang berisi reviewnya, dapat merusak pembacaan file csv \n
jadi data memiliki total sekitar 4.3 jt data dengan 21 variabel \n
berikut variabel variabelnya:\n
- _c0: index dari data\n
- appid: id dari game yang di review\n
- reccomendation id: id dari review\n
- language: bahasa dari isi reviewnya\n
- timestamp_created: kapan review dibuat dengan format waktu unix\n
- timestamp_updated: kapan review diupdate dengan format waktu unix\n
- voted_up: apakah review merekomendasikan gamenya\n
- votes_up: berapa kali review diberi vote berguna\n
- votes_funny: berapa kali review diberi vote lucu\n
- weighted_vote_score: score seberapa berguna review berdasarkan vote reviewnya\n
- comment_count: berapa banyk comment pada review\n
- steam_purchase: apakah reviewer membeli gamenya lewat steam\n
- received_for_free: apakah game didaptkan dengan gratis\n
- written_during_early_access: apakah game direview pada saat masa early access\n
- steamid: id dari reviewer\n
- num_games_owned: berapa banyak game yang dimiliki reviewer\n
- num_reviews: berapa banyak reviews yang telah dibuat reviewer\n
- playtime_forever: total playtime game dari reviewer\n
- playtime_last_two_weeks: total playtime dua minggu terakhir game dari reviewer\n
- playtime_at_review: total playtime game dari reviewer saat review dibikin\n
- last_played: waktu terakhir kali reviewer memaikan game dalam format unix\n
''')
st.subheader('Feature Engineering')
st.markdown('''
pertama kita akan lihat skema dari data:
            df=spark.read.csv("revies.csv",header=True,inferSchema=True)
            df.printSchema()
''')
st.image('skem.png')
st.markdown('''
terus kita akan mengecek untuk missing data dahulu:
            
            df.select([count(when(  col(c).isNull(), c)).alias(c) for c in df.columns]
            ).show()''')
st.image("naan.png")
st.markdown("jadi bisa dilihat bahwa terdapat banyak  data na, tapi karena data hanya akan divisualisasikan maka dapat dibiarkan saja")
st.markdown("""dikarenakan untuk upload file csv ke google looker memiliki maksimal size 100mb maka saya hanya akan mengambil 1 juta data dari data yang 4 juta tersebut\n
                df5=df.filter(df['_c0']<=1000000)""")
st.markdown('''berikut variabel yang akan dihilangkan _c0, recommendationid, timestamp_created, timestamp_updated,steamid, last_played\n
variabel _c0 dihilangkan karena variabel itu hanya merupakan index, recommendationid merupakan id review, jadi semua review memiliki recommendationid yang berbeda maka kurang berguna untuk visualisasi, 
variabel steamid juga dihilangkan karena kebanyak review memiliki reviewer yang berbeda, dan timestamp_created,timestamp_updated, last_played dihilangkan karena waktu terbuatnyta review, kapan terakhir review diupdate, dan kapan terakhir kali reviewer memainkan gamenya merupakan data point yang kurang penting\n
berikut kode untuk menghilangkan kolum tersebut:\n
           df6=df5.drop('_c0',"recommendationid","timestamp_created","timestamp_updated","steamid","last_played") ''')
st.markdown('''
terus karena voted_up dan votes_up memiliki nama yang hampir sama dan dapat membingungkan orang, maka saya akan merubah nama variabel votes_up menjadi votes_helpful\n
            df6=df6.withColumnRenamed('votes_up', 'votes_helpfull')''')
st.markdown('''
terus karena harus dalam bentuk csv maka harus disave menjadi csv dahulu\n
            df6.toPandas().to_csv('mycsv2.csv')''')
st.subheader('Dashboard Visualisasi Data')
st.markdown('''
berikut link untuk google lookernya: https://lookerstudio.google.com/reporting/53d152dc-37fe-44f2-ab4d-3b13614d10b8
''')
st.image('v1.png')
st.image('v2.png')
st.image('v3.png')
st.image('v4.png')
st.subheader('Evaluation and Discussion')
st.markdown('''
jadi google looker merupakan salah satu alat yang sangat berguna untuk visualisasi yang bagus karena cukup mudah digunakan, dengan beberapa 
            cahart yang disediakan dan juga dapat diatur kedalam grafik yang bagus dengan berbagai template dan juga pilihan 
            layout freform atau responsive. \n 
Akan tetapi gogle looker memiliki beberapa kekurangan seperti membutuhkan internet untuk mengaksenya, 
beberapa chart memiliki loading yang lama jika menggunakan data yang besar, jika ingin melakukan analisa lanjutan menggunakan google looker kurang berguna, 
 dan juga beberpa plot juga tidak tersedia pada google looker.\n
jadi google looker merupakan alat yang cukup bagus untuk memvisualisasikan data dengan penampilan yang baik

''')