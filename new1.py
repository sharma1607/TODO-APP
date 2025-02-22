import streamlit as st
import newfunctions

todos_list = newfunctions.get_todos()
def todos():
    new_todo = st.session_state["todo"] + '\n'
    todos_list.append(new_todo)
    newfunctions.updated_list(todos_list)

st.title("TODO APP")
st.subheader("Todos list:")

for index, todo in enumerate(todos_list):
    completed_todo = st.checkbox(todo, key=todo)
    if completed_todo:
        todos_list.pop(index)
        newfunctions.updated_list(todos_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", key="todo", placeholder="add a todoo...",
              on_change=todos)

st.session_state