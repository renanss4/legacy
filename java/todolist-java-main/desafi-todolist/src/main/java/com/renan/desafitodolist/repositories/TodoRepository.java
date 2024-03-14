package com.renan.desafitodolist.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.renan.desafitodolist.entities.Todo;

public interface TodoRepository extends JpaRepository<Todo, Long>{

    
}