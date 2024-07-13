import igorfilmes.calculos.CalculadoraDeTempo;
import igorfilmes.modelos.Filme;
import igorfilmes.modelos.Serie;

public class Principal {
    public static void main(String[] args) {
        Filme meuFilme = new Filme();
        meuFilme.setNome("Carros");
        meuFilme.setAnoDeLancamento(2008);
        meuFilme.setDuracaoEmMinutos(114);
        System.out.println("Duração do Filme: " + meuFilme.getDuracaoEmMinutos());

        meuFilme.exibirFichaTecnica();
        meuFilme.avalia(10);
        meuFilme.avalia(5.5);
        meuFilme.avalia(8);

        System.out.println(meuFilme.getTotalDeAvaliacoes());
        System.out.println(meuFilme.pegaMedia());

        Serie sults = new Serie();
        sults.setNome("Sults");
        sults.setAnoDeLancamento(2010);
        sults.exibirFichaTecnica();
        sults.setTemporada(10);
        sults.setEpisodios(20);
        sults.setMinutosPorEpisodio(80);
        System.out.println("Duração para maratonar: " + sults.getDuracaoEmMinutos());

        CalculadoraDeTempo calculadora = new CalculadoraDeTempo();
        calculadora.inclui(meuFilme);
        calculadora.inclui(sults);
        System.out.println(calculadora.getTempoTotal());
    }
}