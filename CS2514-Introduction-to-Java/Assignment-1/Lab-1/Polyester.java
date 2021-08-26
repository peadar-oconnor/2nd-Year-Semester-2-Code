/**
 * Class for Polyester fabric with behaviour to get the cost 
 * of the fabric. 
 *
 * @author Peadar O'Connor 117302273
 */
public class Polyester extends Synthetic {
    private static final String NAME = "Polyester";
    private static final double COST = 5.0;

    /**
     * Construct an instance of this class with a default name and cost
     * per unit.
     */
    public Polyester( ) {
        super( NAME, COST);
    }
}
