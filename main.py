import streamlit as st
import time



st.title('Streamlit 超入門')

st.write('Display Image')


left, center, right = st.columns(3)

bul = left.button('右に表示')

if bul:
    center.write('Center')

right.write('Right')
right.color_picker('red')
    
prog = st.empty()
bar = st.progress(0)

for i in list(range(100)):
    prog.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

ex = st.expander('問い合わせ')
ex.write('問い合わせ内容を書く')
ex.text_input()

opt = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,10))
)
'あなたの好きな数字は', opt, 'を教えてください'


# txt = st.text_input('aaa')
# txt

# cond = st.slider('bbb',0,100,50)

# cond


# # if st.checkbox('Show Image'):
# #     img = Image.open('unnamed.jpg')
# #     st.image(img)

# st.write('DataFrame')

# # df = pd.DataFrame({
# #     '1列目': [1,2,3,4],
# #     '2列目': [10,50,30,40]
# # })
# # st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#    np.random.randn(100, 2)/[50,50]+[35.69,139.70],
# #    columns=('col %d' % i for i in range(2)))
#    columns=['lat','lon'])
    

# st.dataframe(df.style.highlight_max(axis=0))  # Same as st.write(df)
# st.map(df)
# # st.bar_chart(df)

# """

# # 章
# ## 節
# ### 項


# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')