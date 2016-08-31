<h1>RPG Filler</h1>
<p>
	Programa para automatizar a criação de personagens do RPG D&D 3.5
</p>
<p>
	O RPG Filler é um conjunto de scripts feitos em Python, então para poder executá-lo é necessário ter o Python instalado no seu computador. Caso não tenha acesse <a href="https://www.python.org/">https://www.python.org/</a> para baixar
</p>
<h2>Como utilizar</h2>
<ul>
	<li>
		<h4>Download</h4>
		<p>
			Realize o download zip desse reposítorio e extraia-o em qualquer pasta de seu computador
		</p>
	</li>
	<li>
		<h4>Executar</h4>
		<p>
			Dentro da pasta extraída, há um arquivo chamado "RPGFiller.py". Este é o arquivo 'executável'
		</p>
		<ul>
			<li>
				<h4>Windows</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "python RPGFiller.py"
				</p>
				<ul>
					<li>
						<h5>Erro: "python não é reconhecido como um comando interno"</h5>
						<p>
							Caso ocorra esse erro ao executar o comando "python RPGFiller.py", dê uma olhada nesse <a href="http://stackoverflow.com/questions/7054424/python-not-recognised-as-a-command">fórum</a>
						</p>
					</li>
				</ul>
			</li>
			<li>
				<h4>Linux</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "./RPGFiller.py" ou "python RPGFiller.py"
				</p>
			</li>
		</ul>
	</li>
	<li>
		<h4>Informações sobre o RPG Filler</h4>
		<p>
			O RPG Filler automatiza a criação de um personagem de D&D 3.5 calculando automaticamente o BBA, life e testes de resistência com base nas classes inseridas no personagem. 
			As classes disponíveis são:
		</p>
		<ul>
			<li>Bárbaro</li>
			<li>Bardo</li>
			<li>Clérigo</li>
			<li>Druida</li>
			<li>Guerreiro</li>
			<li>Ladino</li>
			<li>Mago</li>
			<li>Monge</li>
			<li>Paladino</li>
			<li>Ranger</li>
		</ul>
	</li>
</ul>
<h2>DEV's</h2>
<ul>
	<li>
		<h3>Classes Implementadas</h3>
		<ul>
			<li>
				BBA
			</li>
			<li>
				Class
				<ul>
					<li>Bárbaro</li>
					<li>Bardo</li>
					<li>Clérigo</li>
					<li>Druida</li>
					<li>Guerreiro</li>
					<li>Ladino</li>
					<li>Mago</li>
					<li>Monge</li>
					<li>Paladino</li>
					<li>Ranger</li>
				</ul>
			</li>
			<li>
				Personagem
			</li>
			<li>
				Resist
			</li>
			<li>
				Situacao
			</li>
			<li>
				Writer
			</li>
			<li>
				Application
			</li>
			<li>
				MenuBar
			</li>
		</ul>
	</li>
	<li>
		<h3>Persistência de dados</h3>
		<p>
			A persistência foi feita atrávez de arquivos em formato JSON, localizados dentro da pasta "personagens"
		</p>
	</li>
</ul>







