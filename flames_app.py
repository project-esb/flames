import streamlit as st

st.markdown('<center><h1>🅵🅻🅰🅼🅴🆂</h1></center>',unsafe_allow_html=True)

def actual_code():
    s1l=s1.lower()
    s2l=s2.lower()


    s1c=[i for i in s1l if i!=" "]
    s2c=[i for i in s2l if i!=" "]
    s1a=sorted(s1c)
    s2a=sorted(s2c)


    print(s1a)
    print(s2a)

    for _ in range(2):
        for i in s1a:
            t1=i
            for j in s2a:
                t2=j
                if t1==t2:
                    try:
                        s1a.remove(t1)
                        s2a.remove(t2)
                    except ValueError:
                        pass
                else:
                    pass


    n=len(s1a)+len(s2a)


    t=['F','L','A','M','E','S']
    n=len(s1a)+len(s2a)
    p=0
    while(len(t)!=1):
        p = p+(n%len(t))-1
        if(p==-1):
            p=p+len(t)
        if(p>=len(t)):
            p=p%len(t)
        t.remove(t[int(p)])
    ref={
        'F':'Friends',
        'L':'Love',
        'A':'Affection',
        'M':'Marriage',
        'E':'Enemies',
        'S':'Sibling'
    }
    print(ref[t[0]])







with st.form("my_form",clear_on_submit = False):
    s1=st.text_input("Enter Your Name:")
    s2=st.text_input("Enter Your Crush Name:")
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        actual_code()
       



        

    










