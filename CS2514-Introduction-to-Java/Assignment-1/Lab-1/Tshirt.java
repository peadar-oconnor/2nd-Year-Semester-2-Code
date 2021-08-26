/**
 * Class for t-shirts with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public class Tshirt extends Shirt {
    private static final String NAME = "T-shirt";
    private static final double FABRIC_UNITS = 1.5;
    private static final Cotton COTTON = new Cotton( );

    /**
     * Construct an instance of this class with a default name, fabric
     * amd units
     */
    public Tshirt( ) {
        super( NAME, COTTON, FABRIC_UNITS);
    }
}

