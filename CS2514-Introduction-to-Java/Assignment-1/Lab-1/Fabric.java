/**
 * Class for fabric with given name, cost per unit of fabric, default 
 * environmental tax and behaviour to calculate the cost.
 *
 * @author Peadar O'Connor 117302273
 */
public abstract class Fabric {
    private static final double TAX = 2.0;
    private final double tax;
    private final String name;
    private final double cost;

    /**
     * Construct an instance of this class with a given name and 
     * cost per unit.
     *
     * @param name The name of the fabric instance.
     * @param cost The cost per unit of the instance.
     */
    public Fabric( final String name, final double cost ) {
        this.name = name;
        this.cost = cost;
        this.tax = TAX;
    }
    
    /**
     * Get the cost per unit of the instance.
     *
     * @return The cost of the instance.
     */
    public double getCost( ) {
        return cost;
    }

    /**
     * Get the name of this instance.
     *
     * @return The name of the instance.
     */
    public String getName( ) {
        return name;
    }

    /**
     * Get the environmental tax value of the instance.
     *
     * @return The tax of the instance.
     */
    public double getTax( ) {
        return tax;
    }

    /**
     * Abstract class to be overidden in subclasses to get source.
     */ 
    //(If this was only in Natural I couldn't access the 
    // method in Garment, I didnt know how to have it only in Natural)
    public abstract String getSource( );

    /**
     * Calculate the price of the fabric using cost of unit of 
     * fabric times the number of units.
     *
     * @param units The number of units of fabric the instance is made of.
     * @return The calculated price of the fabric.
     */
    public double calcPrice( double units ) {
        return cost*units;
    }
}
