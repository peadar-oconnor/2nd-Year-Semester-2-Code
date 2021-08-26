/**
 * Class for natural fabrics with a given source, and behaviour to 
 * calculate the cost.
 *
 * @author Peadar O'Connor 117302273
 */
public abstract class Natural extends Fabric {
    private final String source;

    /**
     * Construct an instance of this class with a given name, cost
     * per unit and source.
     *
     * @param name The name of the instance.
     * @param cost The cost per unit of fabric for this instance.
     * @param source The source of fabric for this instance.
     */
    public Natural( final String name, final double cost, 
                      final String source ) {
        super( name, cost );
        this.source = source;
    }

    /**
     * Get the source of this instance.
     *
     * @return The source of this instance.
     */
    @Override
    public String getSource( ) {
        return source;
    }

}
