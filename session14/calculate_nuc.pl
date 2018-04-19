#!/usr/bin/perl
 
use strict;
use warnings;
 
my $usage = "Usage: $0 <fasta.fa>\n";
my $infile = shift or die $usage;
 
my $seq = '';
 
open (IN, $infile) or die "Can't open $infile\n";
while (<IN>){
   chomp;
   next if (/^$/);
   if (/^>(.*)$/){
      next;
   }
   else {
      $seq .= $_;
   }
}
close(IN);
 
my ($a,$c,$g,$t,$other) = parseSeq($seq);
 
my $total = $a + $c + $g + $t;
my $gc = sprintf("%.2f",($c + $g) * 100 / $total);
my $at = sprintf("%.2f",($a + $t) * 100 / $total);
 
print "Length = ", length($seq), "\n";
print "A: $a\n";
print "C: $c\n";
print "G: $g\n";
print "T: $t\n";
print "Other: $other\n";
 
print "GC: $gc\n";
print "AT: $at\n";
 
sub parseSeq {
   my ($seq) = @_;
   my $a = '0';
   my $c = '0';
   my $g = '0';
   my $t = '0';
   my $other = '0';
   for (my $i = 0; $i < length($seq); ++$i){
      my $base = substr($seq,$i,1);
      if ($base =~ /a/i){
         ++$a;
      } elsif ($base =~ /c/i){
         ++$c;
      } elsif ($base =~ /g/i){
         ++$g;
      } elsif ($base =~ /t/i){
         ++$t;
      } else {
         ++$other;
      }
   }
   return ($a,$c,$g,$t,$other);
}
