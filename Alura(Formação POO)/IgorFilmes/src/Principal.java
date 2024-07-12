import igorfilmes.modelos.Filme;

public class Principal {
    public static void main(String[] args) {
        Filme meuFilme = new Filme();
        meuFilme.setNome("Carros");
        meuFilme.setAnoDeLancamento(2008);
        meuFilme.setDuracaoEmMinutos(114);

        meuFilme.exibirFilme();
        meuFilme.avalia(10);
        meuFilme.avalia(5.5);
        meuFilme.avalia(8);

        System.out.println(meuFilme.getTotalDeAvaliacoes());
        System.out.println(meuFilme.pegaMedia());
    }
}