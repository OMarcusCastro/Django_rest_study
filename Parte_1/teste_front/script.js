const alunosList = document.getElementById('alunos');

fetch('http://localhost:8000/alunos/')
    .then(response => response.json())
    .then(data => {
        data.forEach(aluno => {
            const li = document.createElement('li');
            li.textContent = `${aluno.nome}-${aluno.cpf}`;
            alunosList.appendChild(li);
            console.log(aluno)
        });
    })
    .catch(error => {
        console.error('Erro ao buscar dados da API:', error);
    });
