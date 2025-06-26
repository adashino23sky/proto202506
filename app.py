import streamlit as st
import streamlit.components.v1 as components

if not "initializing_state" in st.session_state:
    st.session_state.initializing_state = 1

def transfer1to2():
    st.session_state.initializing_state = 2
    # st.rerun() # on_clickでは自動的に実行
    
def chatpage1():
    st.title("chatbot")
    st.button("click to next page",
              key = "check1",
              on_click = transfer1to2
              )

def chatpage2():
    st.title("2ページ目")
    components.html("""
                    <script>
                    alert("Hello from JavaScript!");
                    </script>
                    <h1>This is a custom HTML component</h1>
                    """)

def errorpage():
    st.markdown("Something wrong so that app cannot show any page.")

def main():
    if st.session_state.initializing_state == 1:
        chatpage1()
    elif st.session_state.initializing_state == 2:
        chatpage2()
    else:
        errorpage()

if __name__ == "__main__":
    main()
