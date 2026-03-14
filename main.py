import streamlit as st
from gtts import gTTS
import os
st.title('Tàu hàng liều lĩnh đi qua eo biển Hormuz vì lợi nhuận cao')
tin1 = 'Các công ty có thể kiếm hàng triệu USD cho mỗi chuyến tàu qua eo biển Hormuz, bất chấp phí bảo hiểm và lương thủy thủ cao.'
st.write(tin1)
tin2 = 'Ngày 13/3, Reuters trích dữ liệu của các công ty theo dấu tàu biển Lloyd’s List Intelligence và MarineTraffic cho thấy ít nhất 10 tàu do các công ty Hy Lạp vận hành và ít nhất 2 tàu do Trung Quốc vận hành đã đi qua eo biển Hormuz từ khi xung đột tại Trung Đông xảy ra ngày 28/2. Số tàu này chở cả dầu và hàng hóa thông thường.'
st.write(tin2)
anh = 'https://vcdn1-kinhdoanh.vnecdn.net/2026/03/14/iran-tanker-1773463485-7413-1773463537.jpg?w=1020&h=0&q=100&dpr=1&fit=crop&s=15Z1hbmaE7I07DyqFJMQqA'
st.image(anh, caption = 'Các tàu dầu ở vùng biển gần eo biển Hormuz ngày 11/3. Ảnh: Reuter')
if st.button('Doc noi dung'):
  tts = gTTS(text = tin1 + tin2, lang = 'vi')
  output_file = 'output.mp3'
  tts.save('ouput_file.mp3')
  audio_file = open(output_file, 'rb')
  audio_byte = audio_file.read()
  st.audio(audio_byte, format = 'audio/mp3')
st.write('video minh hoa')
st.video('https://www.youtube.com/watch?v=gJ9sxOwsq0Y')
