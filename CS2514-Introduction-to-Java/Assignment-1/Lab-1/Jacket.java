/**
 * Class for jackets with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public class Jacket extends Coat {
    private static final String NAME = "Jacket";
    private static final double FABRIC_UNITS = 2.0;
    private static final Tweed TWEED = new Tweed( );

    /**
     * Construct an instance of this class with a default name, fabric
     * and units.
     */
    public Jacket( ) {
        super( NAME, TWEED, FABRIC_UNITS);
    }
}

