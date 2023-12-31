import streamlit as st
import pandas as pd

st.markdown(
  """
  Selamat datang di dashboard Langgeng Pambudi!
  """
)

st.title('Belajar Analisis Data :sparkles:')


with st.sidebar:

	st.text(
		'Pengembangan Dashboard')
	st.write(
		'Berikut adalah dashboard sederhana yang coba saya buat dari data yang sudah saya analisis.'
	  	'Ini adalah data kualitas udara dari daerah Wanliu pada tahun 2017.'
		)

tab1, tab2, tab3, tab4, tab5, tab6, = st.tabs(["PM2.5", "RAIN", "WSPM", "PM2.5 perhari", "PM2.5 terendah", "RAIN 21", ])

with tab1:
	st.header("PM2.5 Wanliu dalam feb 2017")
	st.image("https://64.media.tumblr.com/2424478e8c404343623e86acf6f5d340/19061dfaaa1325ce-80/s2048x3072/b352d9e15326d4ea7228310463bf1c468779c03d.pnj")
	st.write("Berdasarkan data, polusi PM2.5 di Wanliu cenderung fluktuatif dengan rata-rata 68.28. Akan tetapi terdapat beberapa hari dengan nilai harian per jam polusi PM2.5 nya yang rendah dibandingkan dengan hari lain. Hari tersebut adalah pada tanggal 9 dan 10 feb 2017. Rata-rata polusi PM2.5 untuk tanggal 9 adalah 5 dan untuk tanggal 10 adalah 5.4.")



with tab2:
	st.header("Hujan (Rain) Wanliu dalam feb 2017")
	st.image("https://64.media.tumblr.com/7e0a3c3fe42b4541e212729ac48f70ea/19061dfaaa1325ce-04/s1280x1920/2fa37eb31c799e43e401ed3a158bf1fef1e692ab.pnj")
	st.write("Curah hujan di daerah Wanliu pada bulan Februari 2017 sangat rendah. Hal tersebut dibuktikan dengan hujan yang turun pada sangat sedikit yaitu hanya pada tanggal 21 Februari 2017. Hujan turun sekitar pukul 13.00-15.00 dan 19.00-23.00 waktu setempat. Hujan pada tanggal tersebut juga intensitasnya ringan dengan nilai tertingginya 1 mm.")

with tab3:
	st.header("Kecepatan Angin (WSPM) Wanliu dalam feb 2017")
	st.image("https://64.media.tumblr.com/f6429331416f0dd6098d2c8351a59c90/19061dfaaa1325ce-c0/s2048x3072/c556e3d9681299251df416ab08aa66c9635cf122.pnj")


with tab4:
	st.header("PM2.5 per jam per hari Wanliu dalam feb 2017")
	st.image("https://64.media.tumblr.com/ca0400524ba154b0bfc05ebefa48f5ab/19061dfaaa1325ce-68/s2048x3072/9da0deacf248e22db6d47b2639562107ff10195c.pnj")
	st.write("Berdasarkan data, polusi PM2.5 di Wanliu cenderung fluktuatif dengan rata-rata 68.28. Akan tetapi terdapat beberapa hari dengan nilai harian per jam polusi PM2.5 nya yang rendah dibandingkan dengan hari lain. Hari tersebut adalah pada tanggal 9 dan 10 feb 2017. Rata-rata polusi PM2.5 untuk tanggal 9 adalah 5 dan untuk tanggal 10 adalah 5.4.")


with tab5:
	st.header("PM2.5 terendah Wanliu dalam feb 2017")
	st.image("https://64.media.tumblr.com/9ede6f88f0a4e554401bb0ebde47fe35/19061dfaaa1325ce-5b/s2048x3072/d0acab83de098842757ef9fa4dc75b8b89ac1949.pnj")


with tab6:
	st.header("Hujan (Rain) pada tanggal 21 feb 2017")
	st.image("https://64.media.tumblr.com/390c98b35584347e5ff01c391f08f01b/19061dfaaa1325ce-28/s1280x1920/2a90ec662e6bfcea4b724065802ef665c908041d.pnj")



