/**
 * Class for winter coats with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public class WinterCoat extends Coat {
    private static final String NAME = "Winter Coat";
    private static final double FABRIC_UNITS = 2.5;
    private static final Polyester POLYESTER = new Polyester( );

    /**
     * Construct an instance of this class with a default name, fabric
     * and units.
     */
    public WinterCoat( ) {
        super( NAME, POLYESTER, FABRIC_UNITS);
    }
}

