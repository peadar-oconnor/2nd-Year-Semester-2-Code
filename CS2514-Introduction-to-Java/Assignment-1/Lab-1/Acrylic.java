/**
 * Class for Acrylic fabric with behaviour to get the cost of the fabric.
 * 
 * @author Peadar O'Connor 117302273
 */
public class Acrylic extends Synthetic {
    private static final String NAME = "Acrylic";
    private static final double COST = 6.0;

    /**
     * Construct an instance of this class with a default name and cost
     * per unit.
     */
    public Acrylic( ) {
        super( NAME, COST);
    }
}

