package com.vila.morador;

import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import com.vila.pet.Pet;
import com.vila.unidade.Unidade;
import com.vila.veiculo.Veiculo;

@Entity
@Table
public class Morador {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	
	@Column
	private String nome;
	private String cpf;
	private String dataNascimento;
	private Integer telefone;
	private String email;

	@OneToMany(cascade = CascadeType.ALL)
	@JoinColumn(name = "moradorId", referencedColumnName = "id")
	private List<Pet> pet;
	
	@OneToMany(cascade = CascadeType.ALL)
	@JoinColumn(name = "moradorId", referencedColumnName = "id")
	private List<Veiculo> veiculo;

	@ManyToOne(cascade = CascadeType.ALL)
	@JoinColumn(name = "UnidadeId", referencedColumnName = "id")
	private Unidade unidade;
	
	public Morador() {
		super();
	}
	
	public Morador(Integer id, String nome, String cpf, String dataNascimento, Integer telefone, String email) {
		super();
		this.id = id;
		this.nome = nome;
		this.cpf = cpf;
		this.dataNascimento = dataNascimento;
		this.telefone = telefone;
		this.email = email;
	}
	
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCpf() {
		return cpf;
	}
	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	public String getDataNascimento() {
		return dataNascimento;
	}
	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}
	public Integer getTelefone() {
		return telefone;
	}
	public void setTelefone(Integer telefone) {
		this.telefone = telefone;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}

	public List<Pet> getPet() {
		return pet;
	}

	public void setPet(List<Pet> pet) {
		this.pet = pet;
	}

	public List<Veiculo> getVeiculo() {
		return veiculo;
	}

	public void setVeiculo(List<Veiculo> veiculo) {
		this.veiculo = veiculo;
	}

	public Unidade getUnidade() {
		return unidade;
	}

	public void setUnidade(Unidade unidade) {
		this.unidade = unidade;
	}
	
	
	
}
