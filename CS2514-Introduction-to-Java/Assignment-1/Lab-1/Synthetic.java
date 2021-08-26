/**
 * Class for synthetic fabrics with overidden behaviour to 
 * calculate the cost and get the source.
 *
 * @author Peadar O'Connor 117302273
 */
public abstract class Synthetic extends Fabric {

    /**
     * Construct an instance of this class with a given name, cost
     * per unit.
     *
     * @param name The name of the instance.
     * @param cost The cost per unit of fabric for this instance.
     */
    public Synthetic( final String name, final double cost ) {
        super( name, cost );
    }

    /**
     * Get the source of this instance, synthetic fabrics have none.
     *
     * @return The source of this instance.
     */
    @Override
    public String getSource( ) {
        String source = "No source";
        return source;
    }

    /**
     * Calculate the cost of the fabric using cost of unit of fabric 
     * times the number of units, plus the environmental tax.
     *
     * @param units The number of units of fabric the instance is made of.
     * @return The calculated price of the fabric.
     */
    @Override
    public double calcPrice( final double units ) {
        return ( getCost( ) + getTax( ) ) * units;
    }
}

