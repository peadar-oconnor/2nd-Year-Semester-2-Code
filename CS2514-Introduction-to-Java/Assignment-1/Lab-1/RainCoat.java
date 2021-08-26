/**
 * Class for rain coats with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public class RainCoat extends Coat {
    private static final String NAME = "Rain coat";
    private static final double FABRIC_UNITS = 2.5;
    private static final Acrylic ACRYLIC = new Acrylic( );

    /**
     * Construct an instance of this class with a default name, fabric
     * and units
     */
    public RainCoat( ) {
        super( NAME, ACRYLIC, FABRIC_UNITS);
    }
}

