&nbsp; Uso de urls.py em apps(home, por exemplo)

>* **Aninhamento de caminhos.**

&nbsp; &nbsp;*Include*

## Renderizando HTML

- Criar uma pasta templates no app.
- Usa o settings para especificar o caminho.
- Uso da biblioteca render
- Add o app no settings/INSTALLED_APPS
- NameSpace evita a colisão de dois arquivos de mesmo nome.
> App Home: Possui arquivo home.html<br>
> App Blog: Possui arquivo home.html

***Solução se dá quando cria-se uma pasta e agora justifica de onde vem esse arquivo no render()***
> App Blog: render(Request, 'blog/home.html')