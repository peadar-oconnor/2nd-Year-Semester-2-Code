/**
 * Class for garments with behaviour to print its purpose, to 
 * calculate the price of the garment, and to print an itemised bill.
 * 
 * @author Peadar O'Connor 117302273
 */
public abstract class Garment {
    private final String name;
    private final String purpose;
    private final Fabric fabric;
    private final double units;
    private final double price;

    /**
     * Construct an instance of this class with a given name, purpose
     * fabric and units.
     *
     * @param name The name of the instance.
     * @param purpose The instance's purpose.
     * @param fabric The type of fabric the instance is made of.
     * @param units How many units of fabric needed to make the instance.
     */
    public Garment( final String name, final String purpose, 
                     final Fabric fabric, final double units ) {
        this.name = name;
        this.purpose = purpose;
        this.fabric = fabric;
        this.units = units;
        this.price = calcPrice();
    }

    /**
     * Get the name of this instance.
     *
     * @return The name of this instance.
     */
    public String getName( ) {
        return name;
    }

    /**
     * Get the purpose of this instance.
     *
     * @return The purpose of this instance.
     */
    public String getPurpose( ) {
        return purpose;
    }

    /**
     * Get the fabric of this instance.
     *
     * @return The fabric the instance is made of.
     */
    public Fabric getFabric( ) {
        return fabric;
    }

    /**
     * Get the units of fabric needed for this instance.
     *
     * @return The units of fabric needed to make the instance
     */
    public double getUnits( ) {
        return units;
    }


    /**
     * Get the price of this instance.
     *
     * @return The total price of this instance.
     */
    public double getPrice( ) {
        return price;
    }

    /**
     * Prints the instance's purpose.
     */
    public void printPurpose( ) {
        System.out.println(getName( ) + ": " + this.getPurpose( ) );
    }

    /**
     * Calculate the total price using the fabric's calcPrice method.
     *
     * @return Total cost of the garment
     */
    public double calcPrice( ) {
        return fabric.calcPrice( units );

    }
    
    /**
     * Prints an itemised bill including information like the name, 
     * fabric, units and source, with calculations for the base and 
     * total price.
     */
    public void printItemisedBill( ) {
        final String nameSentence;
        String detailsSentence;
        final String taxSentence;
        final String baseSentence;
        final String totalSentence;
        nameSentence = "Itemised bill for " + name;
        detailsSentence = "Made of " + getUnits( ) + " units of " + 
                           fabric.getName( );
        if (fabric instanceof Natural) {
            detailsSentence += " made of " + fabric.getSource( );
            taxSentence = "\tenvironment tax: " + fabric.getTax( ) + 
                           " * 0.0 = 0.0";
            baseSentence = "\tbase price: " + getUnits( ) + 
                           " * " + fabric.getCost( ) + " = " + 
                           getPrice( );
            totalSentence = "\tgrand total: " + getUnits( ) +
                           " * " + fabric.getCost( ) + " = " +
                           getPrice( );
        } else {
            taxSentence = "\tenvironment tax: " + fabric.getTax( ) +
                          " * 1.0 = " + fabric.getTax( );
            final double basePrice = getUnits( ) * fabric.getCost( );
            baseSentence = "\tbase price: " + getUnits( ) +
                           " * " + fabric.getCost( ) + " = " +
                           basePrice;
            totalSentence = "\tgrand total: ( " + fabric.getCost( ) + 
                            " + " + fabric.getTax( ) + " ) * " +
                            getUnits( ) + " = " + getPrice( );
        }
        
        System.out.println( nameSentence );
        System.out.println( detailsSentence );
        System.out.println( taxSentence );
        System.out.println( baseSentence );
        System.out.println( totalSentence );
        System.out.println( );
    }

    @Override
    public String toString( ) {
        return getName( );
    }
}
