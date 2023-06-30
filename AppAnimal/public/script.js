async function carregarAnimais(){
    const response = await axios.get('http://localhost:8000/animais/');
    const animais = response.data //cria uma lista com todos os animais cadastrados

    const lista = document.getElementById('lista-animais'); //identifica no html o componente que está sendo modificado

    //acessando cada item da lista animais, só assim podemos acessar cada informação individualmente
    animais.forEach(animal => {
        const item = document.createElement('li'); //cria um item do tipo li
        item.innerText = animal.id; //o item li, recebe a informação nome de cada elemento(animal da lista animais) do backend
        lista.appendChild(item);//acrescenta a lista lu do html, cada item li, que pegamos pela api
        const id_animal = animal.id;
    });
    
}

async function manipularFormulario(){
    const form_animal = document.getElementById('form-animal'); //pegando formulário pelo id
    const input_animal = document.getElementById('nome'); //conectar no componente
    const input_idade = document.getElementById('idade');
    const input_sexo = document.getElementById('sexo');
    const input_cor = document.getElementById('cor');

    form_animal.onsubmit = async (event) => {
        //event.preventDefault(); //pra pagina atualizar sempre que submeter o form
        const nome_animal  = input_animal.value;
        const idade_animal = input_idade.value;
        const sexo_animal = input_sexo.value;
        const cor_animal = input_cor.value;

        const lista = document.getElementById('lista-animais');

        //mandar valores pro backend
        await axios.post('http://localhost:8000/novo_animal/', {
            nome: nome_animal,
            idade: idade_animal,
            sexo: sexo_animal,
            cor: cor_animal,
        });
        const item = document.createElement('li'); //cria um item do tipo li
        item.innerText = animal.nome //o item li, recebe a informação nome de cada elemento(animal da lista animais) do backend
        lista.appendChild(item); 


    }
}

function vendopeloID(){
    
    const id_animal = animal.id;
    const pet = axios.get(`http://localhost:8000/novo_animal/${id_animal}`);
    const colecao = document.getElementById('animal-especifico');

    const it = document.createElement('li');
    it.innerText = pet; 
    colecao.appendChild(item);

   

}



function app(){
    console.log("app iniciada");
    carregarAnimais();
    manipularFormulario();
    vendopeloID();

}

app()