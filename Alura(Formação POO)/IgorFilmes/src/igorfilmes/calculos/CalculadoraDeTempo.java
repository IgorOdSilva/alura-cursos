package igorfilmes.calculos;

import igorfilmes.modelos.Filme;
import igorfilmes.modelos.Serie;
import igorfilmes.modelos.Titulo;

public class CalculadoraDeTempo {
    private int tempoTotal;

    public int getTempoTotal() {
        return this.tempoTotal;
    }

    public void inclui(Titulo titulo){
        this.tempoTotal += titulo.getDuracaoEmMinutos();
    }

}
