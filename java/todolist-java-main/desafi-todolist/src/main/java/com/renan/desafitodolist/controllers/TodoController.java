package com.renan.desafitodolist.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.renan.desafitodolist.entities.Todo;
import com.renan.desafitodolist.services.TodoService;

import jakarta.validation.Valid;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@RestController
@RequestMapping("/todos")
public class TodoController {
    
    private TodoService todoService;

    public TodoController(TodoService todoService) {
        this.todoService = todoService;
    }

    @PostMapping   
    List<Todo> create(@RequestBody @Valid Todo todo) {
        return todoService.create(todo);
    }

    @GetMapping
    List<Todo> list() {
        return todoService.list();
    }

    @PutMapping
    List<Todo> update(@RequestBody Todo todo) {
        return todoService.update(todo);
    }

    @DeleteMapping("{id}")
    List<Todo> delete(@PathVariable(value = "id") Long id) {
        return todoService.delete(id);
    }
}
