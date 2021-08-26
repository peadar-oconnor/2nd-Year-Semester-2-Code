/**
 * Class for Tweed fabric with behaviour to get the cost of the fabric. 
 *
 * @author Peadar O'Connor 117302273
 */
public class Tweed extends Natural {
    private static final String NAME = "Tweed";
    private static final double COST = 3.0;
    private static final String SOURCE = "Wool";

    /**
     * Construct an instance of this class with a given name, cost
     * per unit and source.
     */
    public Tweed( ) {
        super( NAME, COST, SOURCE);
    }
}

