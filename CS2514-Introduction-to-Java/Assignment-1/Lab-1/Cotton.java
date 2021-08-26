/**
 * Class for Cotton fabric with behaviour to get the cost of the fabric. 
 *
 * @author Peadar O'Connor 117302273
 */
public class Cotton extends Natural {
    private static final String NAME = "Cotton";
    private static final double COST = 2.0;
    private static final String SOURCE = "Gossypium";

    /**
     * Construct an instance of this class with a given name, cost
     * per unit and source.
     */
    public Cotton( ) {
        super( NAME, COST, SOURCE);
    }
}
