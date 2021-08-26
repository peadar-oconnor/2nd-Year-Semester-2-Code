/**
 * Class for shirts with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public abstract class Shirt extends Garment {
    private static final String DEFAULT_PURPOSE = "Cover the body";

    /**
     * Construct an instance of this class with a given name, fabric,
     * units, and a default purpose.
     *
     * @param name The name of the instance.
     * @param fabric The type of fabric the instance is made of.
     * @param units How many units of fabric needed to make the instance.
     */
    public Shirt( final String name, final Fabric fabric, 
                   final double units ) {
        super( name, DEFAULT_PURPOSE, fabric, units );
    }

}
