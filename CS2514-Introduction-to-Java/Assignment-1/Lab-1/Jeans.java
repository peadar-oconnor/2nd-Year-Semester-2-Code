/**
 * Class for jeans with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */ 
public class Jeans extends Trousers {
    private static final String NAME = "Jeans";
    private static final double FABRIC_UNITS = 2.0;
    private static final Fabric COTTON = new Cotton( );

    /**
     * Construct an instance of this class with a default name, fabric
     * and units.
     */
    public Jeans( ) {
        super( NAME, COTTON, FABRIC_UNITS);
    }
}
