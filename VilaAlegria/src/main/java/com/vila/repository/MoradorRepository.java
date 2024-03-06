package com.vila.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.vila.morador.Morador;

@Repository
public interface MoradorRepository extends JpaRepository<Morador, Integer>{
	
	Optional<Morador>findMoradorByNome(String nome);
	
	Morador findMoradorById(Integer id);
}
