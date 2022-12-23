import React from 'react';
import { useDispatch } from "react-redux";
import { deleteTodo } from "../reducers/todo.reducer";

const Todo = ({ id, text }) => {

	const dispatch = useDispatch();

	const onClick = e => {
		e.preventDefault()
		dispatch(
			deleteTodo({
				id: id
			})
		)
	}

	return (
		<li className="task-item">
			<div>
				{id} | {text}
			</div>
			<div>
				<button className="remove-task-button" onClick={onClick}>Delete</button>
			</div>
		</li>
	);
};

export default Todo;