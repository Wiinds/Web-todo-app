import streamlit as st
import Todo_Functions

todos = Todo_Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Todo_Functions.write_todos(todos)
    

st.title("My Todo App")
st.subheader("Welcome to your Web Based To do app!")
#st.write("hello funded trader!")
  
  
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        Todo_Functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()
    
    
st.text_input(label="Type here", placeholder="Enter a Todo!", 
              label_visibility="hidden",
              on_change=add_todo, key="new_todo")




