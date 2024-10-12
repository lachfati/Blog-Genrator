import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def write_blog(topic,no_words,blog_style):
    ##LLama 2 model
    llm=CTransformers(model='C:/Users/Lachhab Fatima/Downloads/llama-2-7b-chat.ggmlv3.q8_0.bin' , model_type='llama' 
                       ,config={'max_new_tokens' :256, 'temperature':0.01}
                       )
    
    template="""
        Write a blog for {blog_style} job profile for a topic {topic}
        within {no_words} words.
            """      
    prompt = PromptTemplate(input_variables = ['blog_style','topic','no_words'], template=template)

    ## generate the response using llama
    formatted_prompt = prompt.format(blog_style=blog_style, topic=topic, no_words=no_words)
    response = llm(formatted_prompt)    
    print(response)
    return response



st.set_page_config(page_title='Genreate Blogs :sheet:',page_icon=':memo:',layout='centered',
                    initial_sidebar_state='collapsed')
st.header('Genreate Blogs :memo:')
input_text=st.text_input('What is the topic of your blog ?')

col1,col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("enter number of words that you want")
with col2:
    blog_style = st.selectbox('writing the blog for :',('Data Science','AI','Researchers'),index=0 )

if st.button('Genrerate'):
    st.write(write_blog(input_text,no_words,blog_style))